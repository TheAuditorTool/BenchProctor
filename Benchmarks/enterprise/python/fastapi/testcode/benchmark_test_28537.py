# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest28537(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
