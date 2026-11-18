# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
import jsonschema
from starlette.responses import JSONResponse


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


@app.post("/BenchmarkTest00424")
async def BenchmarkTest00424(request: Request):
    auth_header = request.headers.get('authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.\\-]+$"})
    except jsonschema.ValidationError:
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    request.session['data'] = str(processed)
    return {"updated": True}
