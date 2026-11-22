# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
from urllib.parse import urlparse
from pydantic import BaseModel
from starlette.responses import JSONResponse
import re


class UserInput(BaseModel):
    payload: str = ''

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00025")
async def BenchmarkTest00025(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    requests.get(str(target_url))
    return {"updated": True}
