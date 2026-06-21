# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest00790(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
