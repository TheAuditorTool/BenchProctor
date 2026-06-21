# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest28180(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    return RedirectResponse(url=str(data))
