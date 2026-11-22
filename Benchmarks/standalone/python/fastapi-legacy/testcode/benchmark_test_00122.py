# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from http.cookies import SimpleCookie
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


@app.post("/BenchmarkTest00122")
async def BenchmarkTest00122(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    cookie = SimpleCookie()
    cookie['session'] = str(data)
    cookie['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    resp = JSONResponse({'status': 'ok'})
    resp.headers.append('set-cookie', cookie['session'].OutputString())
    return resp
