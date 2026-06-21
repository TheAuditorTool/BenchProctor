# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest18084(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
