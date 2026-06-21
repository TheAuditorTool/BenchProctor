# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest52881(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
