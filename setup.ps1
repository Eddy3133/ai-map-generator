# Setup script for AI Map Generator

Write-Host "Setting up AI Map Generator..." -ForegroundColor Green

# Setup Backend
Write-Host "`nSetting up backend..." -ForegroundColor Cyan
cd backend
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate
Write-Host "Installing Python dependencies..."
pip install -r requirements.txt

# Create .env if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "`nCreating .env file..."
    Copy-Item ".env.example" ".env"
    Write-Host "Please edit .env and add your OpenAI API key" -ForegroundColor Yellow
}

# Setup Frontend
Write-Host "`nSetting up frontend..." -ForegroundColor Cyan
cd ..\frontend
Write-Host "Installing Node.js dependencies..."
npm install

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "`nTo start the servers:" -ForegroundColor Yellow
Write-Host "1. Backend: cd backend && .\venv\Scripts\activate && uvicorn main:app --reload"
Write-Host "2. Frontend: cd frontend && npm run dev" 