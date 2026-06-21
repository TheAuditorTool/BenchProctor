# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest10843(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
