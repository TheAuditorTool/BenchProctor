# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from fastapi import Form
from starlette.responses import JSONResponse
import re


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00263")
async def BenchmarkTest00263(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return {"updated": True}
