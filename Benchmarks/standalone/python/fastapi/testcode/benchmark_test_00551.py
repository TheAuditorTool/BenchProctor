# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00551")
async def BenchmarkTest00551(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid number'}, status_code=400)
    processed = _coerced
    exec(str(processed))
    return {"updated": True}
