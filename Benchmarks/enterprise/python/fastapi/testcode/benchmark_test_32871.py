# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def ensure_str(value):
    return str(value)

async def BenchmarkTest32871(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ensure_str(multipart_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
