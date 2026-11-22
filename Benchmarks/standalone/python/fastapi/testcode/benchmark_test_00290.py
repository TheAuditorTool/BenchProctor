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
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    reader = make_reader(upload_name)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return {"updated": True}
