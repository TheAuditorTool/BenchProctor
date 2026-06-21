# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest61302(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if str(data).endswith(('/public', '/static', '/.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
