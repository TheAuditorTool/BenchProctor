# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest54442(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
