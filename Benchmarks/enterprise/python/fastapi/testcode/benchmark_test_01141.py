# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest01141(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
