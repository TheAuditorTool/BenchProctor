# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest04803(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
