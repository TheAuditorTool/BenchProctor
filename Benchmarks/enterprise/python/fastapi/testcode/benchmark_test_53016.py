# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest53016(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
