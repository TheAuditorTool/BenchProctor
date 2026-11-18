# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import yaml
from urllib.parse import unquote
from starlette.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00661")
async def BenchmarkTest00661(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    parsed = yaml.safe_load(data)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
