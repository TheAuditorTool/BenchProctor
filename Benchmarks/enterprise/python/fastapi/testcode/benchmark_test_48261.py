# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest48261(request: Request):
    auth_header = request.headers.get('authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
