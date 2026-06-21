# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest48765(request: Request):
    ua_value = request.headers.get('user-agent', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(ua_value))
    return RedirectResponse(url=target)
