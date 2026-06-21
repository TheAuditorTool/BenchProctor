# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest60597(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
