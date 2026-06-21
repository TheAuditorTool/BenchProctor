# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest42928(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    return RedirectResponse(url=str(data))
