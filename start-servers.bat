@echo off
echo Starting AI Map Generator servers...

:: Start the backend server
echo Starting backend server...
cd backend
start cmd /k "C:\Users\pleas\AppData\Local\Programs\Python\Python313\python.exe -m uvicorn main:app --reload"

:: Start the frontend server
echo Starting frontend server...
cd ..\frontend
start cmd /k "npm run dev"

echo Servers are starting...
echo Frontend will be available at: http://localhost:5173
echo Backend will be available at: http://localhost:8000
echo.
echo If you see any errors, please make sure:
echo 1. You have created a .env file in the backend directory with your OpenAI API key
echo 2. Both Python and Node.js are installed
echo.
pause 