# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import re


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest00019(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
