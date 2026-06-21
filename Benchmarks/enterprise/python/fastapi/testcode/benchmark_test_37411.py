# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest37411(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
