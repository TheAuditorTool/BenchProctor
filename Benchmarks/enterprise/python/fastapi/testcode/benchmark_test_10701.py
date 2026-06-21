# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest10701(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
