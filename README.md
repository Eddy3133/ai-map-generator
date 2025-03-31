<<<<<<< HEAD
# AI Map Generator

An interactive web application that generates custom maps using OpenAI's DALL-E 3 API. Users can describe the map they want, choose a style, and receive a unique AI-generated map visualization.

## Features

- Generate custom maps using natural language descriptions
- Multiple map styles (realistic, artistic, cartoon, etc.)
- Real-time image generation
- Responsive web interface
- FastAPI backend with OpenAI integration
- React + TypeScript frontend

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Eddy3133/ai-map-generator.git
cd ai-map-generator
```

2. Set up the backend:
```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

pip install -r requirements.txt
```

3. Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

4. Set up the frontend:
```bash
cd ../frontend
npm install
```

## Running the Application

1. Start the backend server:
```bash
cd backend
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

uvicorn main:app --reload
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Open your browser and navigate to `http://localhost:5173`

## Usage

1. Enter a description of the map you want to generate
2. Select a style for the map
3. Click "Generate Map"
4. Wait for the AI to generate your map
5. View and download the generated map

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the DALL-E 3 API
- FastAPI for the backend framework
- React and TypeScript for the frontend framework 
=======
# ai-map-generator
>>>>>>> 1a15fe720536798e1313f809d1a96defa6f6ebbd
