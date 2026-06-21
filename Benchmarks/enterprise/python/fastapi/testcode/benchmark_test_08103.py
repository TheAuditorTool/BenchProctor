# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from types import SimpleNamespace


async def BenchmarkTest08103(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
