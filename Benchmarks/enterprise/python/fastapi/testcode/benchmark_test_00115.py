# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
from starlette.responses import HTMLResponse


async def BenchmarkTest00115(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
