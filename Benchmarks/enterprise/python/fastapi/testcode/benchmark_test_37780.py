# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


def relay_value(value):
    return value

async def BenchmarkTest37780(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = relay_value(header_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
