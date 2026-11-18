# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
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


@app.post("/BenchmarkTest00007")
async def BenchmarkTest00007(request: Request):
    upload_name = getattr((await request.form()).get('doc'), 'filename', '')
    data = '%s' % str(upload_name)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return {"updated": True}
