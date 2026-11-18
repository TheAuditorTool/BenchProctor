# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import subprocess
from starlette.responses import JSONResponse
from pydantic import Field, ValidationError, create_model


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00046")
async def BenchmarkTest00046(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%\\-]+$")))(value=str(data))
    except ValidationError:
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
