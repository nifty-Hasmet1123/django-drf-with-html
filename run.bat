@echo off
echo Making migrations...
python manage.py makemigrations
IF %ERRORLEVEL% NEQ 0 (
    echo Error during makemigrations. Exiting...
    exit /b %ERRORLEVEL%
)

echo Applying migrations...
python manage.py migrate
IF %ERRORLEVEL% NEQ 0 (
    echo Error during migrate. Exiting...
    exit /b %ERRORLEVEL%
)

echo Starting Django Server...
python manage.py runserver
IF %ERRORLEVEL% NEQ 0 (
    echo Error starting the server. Exiting...
    exit /b %ERRORLEVEL%
)