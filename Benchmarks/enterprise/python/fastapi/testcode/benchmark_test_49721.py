# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest49721(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    if str(data) == 'fluffy':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
