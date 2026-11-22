# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from lxml import etree
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


@app.post("/BenchmarkTest00290")
async def BenchmarkTest00290(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(data) + '"]')
    find_user(tree)
    return {"updated": True}
