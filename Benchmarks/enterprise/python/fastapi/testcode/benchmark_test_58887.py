# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest58887(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
