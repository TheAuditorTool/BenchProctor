# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest58609(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
