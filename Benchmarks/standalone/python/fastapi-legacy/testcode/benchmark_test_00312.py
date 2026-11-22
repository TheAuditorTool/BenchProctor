# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from http.cookies import SimpleCookie
from starlette.responses import JSONResponse
from dataclasses import dataclass


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


@app.post("/BenchmarkTest00312")
async def BenchmarkTest00312(request: Request):
    host_value = request.headers.get('host', '')
    form = FormData(payload=host_value)
    data = form.payload
    cookie = SimpleCookie()
    cookie['session'] = str(data)
    cookie['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    resp = JSONResponse({'status': 'ok'})
    resp.headers.append('set-cookie', cookie['session'].OutputString())
    return resp
