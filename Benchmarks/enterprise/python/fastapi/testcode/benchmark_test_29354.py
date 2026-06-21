# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest29354(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
