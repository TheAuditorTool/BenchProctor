# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest31192(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    normalized = unicodedata.normalize('NFKC', str(raw_body))
    return HTMLResponse('<p>' + normalized + '</p>')
