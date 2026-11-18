# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from lxml import etree
import jsonschema
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


@app.post("/BenchmarkTest00473")
async def BenchmarkTest00473(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%~\\-]+$"})
    except jsonschema.ValidationError:
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return {"updated": True}
