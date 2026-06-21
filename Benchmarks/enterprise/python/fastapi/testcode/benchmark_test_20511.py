# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest20511(request: Request):
    path_value = request.path_params.get('id', '')
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
