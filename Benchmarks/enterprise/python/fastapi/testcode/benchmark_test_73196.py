# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest73196(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
