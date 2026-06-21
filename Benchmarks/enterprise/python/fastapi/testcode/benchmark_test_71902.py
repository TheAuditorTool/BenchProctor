# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest71902(request: Request):
    user_id = request.query_params.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
