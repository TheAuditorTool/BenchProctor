# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest38612(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return HTMLResponse('<div>' + str(processed) + '</div>')
