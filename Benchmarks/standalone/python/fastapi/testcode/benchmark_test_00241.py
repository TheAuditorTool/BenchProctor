# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from lxml import etree
import json
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


@app.post("/BenchmarkTest00241")
async def BenchmarkTest00241(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return {"updated": True}
