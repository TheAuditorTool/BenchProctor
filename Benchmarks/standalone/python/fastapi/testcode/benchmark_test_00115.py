# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from fastapi.responses import JSONResponse


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


@app.post("/BenchmarkTest00115")
async def BenchmarkTest00115(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    return HTMLResponse('<div>' + str(data) + '</div>')
