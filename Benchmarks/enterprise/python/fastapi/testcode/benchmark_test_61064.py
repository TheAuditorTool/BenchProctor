# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest61064(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
