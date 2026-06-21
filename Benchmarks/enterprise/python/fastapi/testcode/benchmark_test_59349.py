# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest59349(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
