# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest29917(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
