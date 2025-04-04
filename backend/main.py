from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
import logging
import traceback

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS middleware configuration
origins = [
    "https://artificial-intelligence-map-generator.netlify.app",
    "http://artificial-intelligence-map-generator.netlify.app",
    "https://eddy3133.github.io",
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

class MapRequest(BaseModel):
    prompt: str
    style: str

@app.post("/generate-map")
async def generate_map(request: MapRequest):
    try:
        logger.info(f"Received request with prompt: {request.prompt} and style: {request.style}")
        
        if not os.getenv("OPENAI_API_KEY"):
            logger.error("OpenAI API key not found")
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        try:
            response = openai.Image.create(
                prompt=f"Generate a {request.style} map of {request.prompt}",
                n=1,
                size="1024x1024"
            )
            logger.info("Successfully generated image")
            return {"url": response["data"][0]["url"]}
            
        except openai.error.AuthenticationError:
            logger.error("OpenAI API authentication failed")
            raise HTTPException(status_code=401, detail="OpenAI API authentication failed")
        except openai.error.RateLimitError:
            logger.error("OpenAI API rate limit exceeded")
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        except Exception as e:
            logger.error(f"OpenAI API error: {str(e)}\n{traceback.format_exc()}")
            raise HTTPException(status_code=500, detail=str(e))
            
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
