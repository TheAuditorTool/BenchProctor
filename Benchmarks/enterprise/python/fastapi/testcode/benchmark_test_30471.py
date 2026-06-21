# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest30471(request: Request):
    user_id = request.query_params.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
