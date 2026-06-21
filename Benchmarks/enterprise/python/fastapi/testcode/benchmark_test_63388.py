# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest63388(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    return RedirectResponse(url=str(data))
