# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest25139(request: Request):
    user_id = request.query_params.get('id', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(user_id)})
