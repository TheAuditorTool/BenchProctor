# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest68707(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    return RedirectResponse(url=str(data))
