# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest58978(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    if str(data) == 'fluffy':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
