# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest14645(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
