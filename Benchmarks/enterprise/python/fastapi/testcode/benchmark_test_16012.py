# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest16012(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
