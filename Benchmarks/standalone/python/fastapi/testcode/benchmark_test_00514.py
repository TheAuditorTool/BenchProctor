# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
import markdown
import bleach
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


@app.post("/BenchmarkTest00514")
async def BenchmarkTest00514(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = bleach.clean(markdown.markdown(data))
    return HTMLResponse('<div>' + str(processed) + '</div>')
