from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
import logging
import traceback
from fastapi.responses import JSONResponse

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# More permissive CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=False,  # Changed to False since we're using allow_origins=["*"]
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.options("/generate-map")
async def options_map():
    return JSONResponse(
        content={"message": "OK"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )

class MapRequest(BaseModel):
    prompt: str
    style: str = "realistic"
    size: str = "1024x1024"

    class Config:
        arbitrary_types_allowed = True

@app.get("/")
async def read_root():
    return {"status": "healthy", "message": "AI Map Generator API"}

@app.post("/generate-map")
async def generate_map(request: MapRequest):
    try:
        logger.info(f"Received request with prompt: {request.prompt}, style: {request.style}")
        
        # Initialize OpenAI client
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error("OpenAI API key not found in environment variables")
            raise ValueError("OpenAI API key not found in environment variables")
            
        logger.info("API Key loaded successfully")
        
        client = openai.OpenAI(api_key=api_key)
        
        # Create the prompt for DALL-E
        prompt = f"Generate a {request.style} map showing {request.prompt}"
        logger.info(f"Generated prompt: {prompt}")
        
        # Generate image using DALL-E
        logger.info("Calling OpenAI API...")
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=request.size,
                quality="standard",
                n=1,
            )
            logger.info("Received response from OpenAI")
            return {"url": response.data[0].url}
        except openai.AuthenticationError as e:
            logger.error(f"OpenAI Authentication Error: {str(e)}")
            raise HTTPException(status_code=401, detail="Invalid OpenAI API key")
        except openai.RateLimitError as e:
            logger.error(f"OpenAI Rate Limit Error: {str(e)}")
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        except openai.APIError as e:
            logger.error(f"OpenAI API Error: {str(e)}")
            raise HTTPException(status_code=500, detail="OpenAI API error")
    
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
