# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest55451(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
