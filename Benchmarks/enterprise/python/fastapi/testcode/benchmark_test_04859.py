# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest04859(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    normalized = unicodedata.normalize('NFKC', str(header_value))
    return HTMLResponse('<p>' + normalized + '</p>')
