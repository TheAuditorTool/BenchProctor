# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import base64
from starlette.responses import HTMLResponse


async def BenchmarkTest12140(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return HTMLResponse('<script src="' + str(data) + '"></script>')
