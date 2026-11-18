# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00283")
async def BenchmarkTest00283(request: Request):
    env_value = os.environ.get('APP_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(env_value).strip()
        case _:
            data = str(env_value)
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
