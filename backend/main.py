from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5176"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(data: dict, response: Response):
    user_id = data.get("id")
    pwd = data.get("pwd")

    if not user_id or not pwd:
        return {"ok": False}

    response.set_cookie(
        key="user",
        value=user_id,
        path="/",
        max_age=60*60*24,
        httponly=False,
        samesite="lax",
        secure=False
    )

    return {"ok": True}
