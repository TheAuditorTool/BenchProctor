# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import subprocess
import re
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


@app.post("/BenchmarkTest00423")
async def BenchmarkTest00423(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
