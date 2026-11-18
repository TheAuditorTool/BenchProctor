# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
from starlette.responses import JSONResponse
from app_runtime import db


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00200")
async def BenchmarkTest00200(request: Request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = '%s' % str(api_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
