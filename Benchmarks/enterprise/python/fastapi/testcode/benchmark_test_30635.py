# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest30635(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    return RedirectResponse(url=str(data))
