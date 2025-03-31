# Start script for AI Map Generator

# Start Backend
Write-Host "Starting backend server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; .\venv\Scripts\activate; uvicorn main:app --reload"

# Start Frontend
Write-Host "Starting frontend server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Write-Host "`nServers are starting..." -ForegroundColor Green
Write-Host "Frontend will be available at: http://localhost:5173"
Write-Host "Backend will be available at: http://localhost:8000" 