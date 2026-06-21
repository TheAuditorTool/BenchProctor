# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest76694(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
