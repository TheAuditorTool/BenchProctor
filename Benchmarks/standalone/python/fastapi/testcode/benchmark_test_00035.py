# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00035/{id}")
async def BenchmarkTest00035(request: Request, id: str):
    path_value = id
    data = ' '.join(str(path_value).split())
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid number'}, status_code=400)
    processed = _coerced
    eval(str(processed))
    return {"updated": True}
