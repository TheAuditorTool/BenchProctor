# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00018")
async def BenchmarkTest00018(request: Request, req: UserInput):
    json_value = req.payload
    reader = make_reader(json_value)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    request.session.update({'data': str(processed)})
    return {"updated": True}
