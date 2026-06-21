# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest30964(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
