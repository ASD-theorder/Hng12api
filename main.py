from fastapi import FastAPI
from datetime import datetime
import pytz # type: ignore
from starlette.middleware.cors
import CORSMiddleware # type: ignore

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    email = "abele4336@gmail.com"
    github_url = "https://github.com/ASD-theorder/Hng12api.git"
    utc_now = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
"email": email,   # type: ignore
"current_datetime":
utc_now,
        "github_url": github_url
    }