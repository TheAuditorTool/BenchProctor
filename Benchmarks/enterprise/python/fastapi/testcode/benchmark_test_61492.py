# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest61492(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    return RedirectResponse(url=str(data))
