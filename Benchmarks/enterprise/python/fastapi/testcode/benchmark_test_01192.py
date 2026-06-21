# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest01192(request: Request):
    referer_value = request.headers.get('referer', '')
    normalized = unicodedata.normalize('NFKC', str(referer_value))
    return HTMLResponse('<p>' + normalized + '</p>')
