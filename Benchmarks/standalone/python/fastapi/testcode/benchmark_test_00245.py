# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pathlib import Path
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


@app.post("/BenchmarkTest00245/{id}")
async def BenchmarkTest00245(request: Request, id: str):
    path_value = id
    data, _sep, _rest = str(path_value).partition('\x00')
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    Path(checked_path).write_text('data')
    return {"updated": True}
