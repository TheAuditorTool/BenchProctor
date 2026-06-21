# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


def ensure_str(value):
    return str(value)

async def BenchmarkTest50295(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
