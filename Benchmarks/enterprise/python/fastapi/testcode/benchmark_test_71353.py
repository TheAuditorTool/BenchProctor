# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest71353(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
