# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest69788(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return HTMLResponse('<img src="' + str(processed) + '">')
