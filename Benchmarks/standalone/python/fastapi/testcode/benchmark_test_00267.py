# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import re
from pathlib import Path


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00267/{id}")
async def BenchmarkTest00267(request: Request, id: str):
    path_value = id
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(path_value).strip()
        case _:
            data = str(path_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    Path('/var/app/data/' + str(processed)).write_text('data')
    return {"updated": True}
