# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest74816(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    return RedirectResponse(url=str(data))
