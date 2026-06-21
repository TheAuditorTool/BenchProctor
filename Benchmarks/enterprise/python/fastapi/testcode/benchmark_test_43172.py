# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest43172(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
