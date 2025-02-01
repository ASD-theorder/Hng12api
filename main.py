from fastapi import FastAPI
from datetime import datetime
import pytz # type: ignore

app = FastAPI()

@app.get("/")
def read_root():
    email = "abele4336@gmail.com"
    github_url = "https://github.com/ASD-theorder/Hng12api.git"
    utc_now = datetime.now(pytz.UTC).isoformat()

    return {
"email": email,   # type: ignore
"current_datetime":
utc_now,
        "github_url": github_url
    }