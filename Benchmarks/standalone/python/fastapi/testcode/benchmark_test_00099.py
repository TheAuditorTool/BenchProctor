# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00099")
async def BenchmarkTest00099(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return JSONResponse({'domain': domain}, status_code=200)
