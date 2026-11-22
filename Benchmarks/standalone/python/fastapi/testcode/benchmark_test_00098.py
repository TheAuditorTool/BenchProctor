# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from lxml import etree
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


@app.post("/BenchmarkTest00098")
async def BenchmarkTest00098(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(processed) + '"]')
    find_user(tree)
    return {"updated": True}
