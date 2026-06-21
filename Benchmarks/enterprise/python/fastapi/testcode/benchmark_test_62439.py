# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def ensure_str(value):
    return str(value)

async def BenchmarkTest62439(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
