# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from urllib.parse import unquote


async def BenchmarkTest14013(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
