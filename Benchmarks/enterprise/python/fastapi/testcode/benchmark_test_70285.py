# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest70285(request: Request):
    referer_value = request.headers.get('referer', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(referer_value))
    return RedirectResponse(url=target)
