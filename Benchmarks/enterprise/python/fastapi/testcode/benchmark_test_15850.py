# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse
import os


async def BenchmarkTest15850(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = str(dotenv_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
