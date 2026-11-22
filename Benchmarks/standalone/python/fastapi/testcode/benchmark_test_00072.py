# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


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


@app.post("/BenchmarkTest00072")
async def BenchmarkTest00072(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
