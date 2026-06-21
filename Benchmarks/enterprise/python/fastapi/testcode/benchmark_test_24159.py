# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest24159(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
