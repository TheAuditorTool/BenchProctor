# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest00401(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(data)})
