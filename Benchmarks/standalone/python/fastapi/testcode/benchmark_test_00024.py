# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00024")
async def BenchmarkTest00024(request: Request):
    upload_name = getattr((await request.form()).get('doc'), 'filename', '')
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
