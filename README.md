## for implementing test only
1. start the backend: (from root)
   - create a virtual environment:`python -m venv venv`
   - `source venv/bin/activate`(enter the virtual environment)
   - `python3 app.py` (start the server)
2. start the frontend: (from root)
   - `cd frontend`
   - `npm start `
3. generate the json_package file:
   - `pip freeze > requirements.txt`
   - `pip install -r requirements.txt` (refresh based on requirements.txt)

## Docker command
1. docker build:
   - `docker build -f Dockerfile.backend -t peggyliao/project_backend:1.0 .` backend
   - `docker build -f Dockerfile.frontend -t peggyliao/project_frontend:1.0 .`frontend
2. docker run:
   - `docker run --rm -p 8888:8888 peggyliao/project_frontend:1.0`frontend
   - `docker run --rm -p 5001:5001 peggyliao/project_backend:1.0` backend