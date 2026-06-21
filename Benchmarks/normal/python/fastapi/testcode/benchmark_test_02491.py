# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest02491(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
