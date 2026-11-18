# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00407")
async def BenchmarkTest00407(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
