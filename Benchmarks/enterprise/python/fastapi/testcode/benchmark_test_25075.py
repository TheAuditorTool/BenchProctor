# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest25075(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(ua_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = ua_value
    logging.info('User action: ' + str(processed))
    return {"updated": True}
