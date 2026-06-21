# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest18912(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
