# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest62261(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
