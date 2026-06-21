# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import re


def relay_value(value):
    return value

async def BenchmarkTest79480(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
