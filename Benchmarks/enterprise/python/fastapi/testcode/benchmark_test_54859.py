# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import HTMLResponse


async def BenchmarkTest54859(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
