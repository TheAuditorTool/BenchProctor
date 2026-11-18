# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import PlainTextResponse
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00605")
async def BenchmarkTest00605(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(multipart_value).strip()
        case _:
            data = str(multipart_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
