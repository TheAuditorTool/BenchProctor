# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest39137(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
