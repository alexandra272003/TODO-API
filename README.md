# Todo API Studio

A standalone frontend for the FastAPI Todo API.

## Your backend contract

- GET `/`
- GET `/ping`
- GET `/todos`
- GET `/todos/completed`
- POST `/todos`
- GET `/todos/{todo_id}`
- PUT `/todos/{todo_id}`
- DELETE `/todos/{todo_id}`

## Run

1. Start your FastAPI backend, for example:
   `uvicorn main:app --reload`

2. Open `index.html` through a local static server (recommended), e.g.:
   `python -m http.server 5500`

3. Visit:
   `http://127.0.0.1:5500`

4. Keep the API URL as:
   `http://127.0.0.1:8000`

If the browser blocks requests because of CORS, add FastAPI CORS middleware to the backend:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

For production, replace `allow_origins=["*"]` with the actual frontend origin.
# TODO-API
