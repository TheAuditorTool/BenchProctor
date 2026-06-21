# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from types import SimpleNamespace


async def BenchmarkTest02971(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return HTMLResponse('<div>' + str(processed) + '</div>')
