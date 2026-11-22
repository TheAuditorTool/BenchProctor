# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
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


@app.post("/BenchmarkTest00074")
async def BenchmarkTest00074(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value!s}'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    Path(checked_path).write_text('data')
    return {"updated": True}
