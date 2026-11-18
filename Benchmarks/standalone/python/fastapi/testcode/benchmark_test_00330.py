# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00330")
async def BenchmarkTest00330(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    form = FormData(payload=xml_value)
    data = form.payload
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid number'}, status_code=400)
    processed = _coerced
    eval(str(processed))
    return {"updated": True}
