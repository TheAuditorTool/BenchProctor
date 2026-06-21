# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest50014(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
