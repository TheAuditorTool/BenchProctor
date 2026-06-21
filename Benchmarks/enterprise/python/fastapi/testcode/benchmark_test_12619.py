# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12619(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
