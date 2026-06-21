# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest72301(request: Request):
    auth_header = request.headers.get('authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
