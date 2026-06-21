# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest40986(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
