# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from app_runtime import db
from fastapi.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00500")
async def BenchmarkTest00500(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return {"updated": True}
