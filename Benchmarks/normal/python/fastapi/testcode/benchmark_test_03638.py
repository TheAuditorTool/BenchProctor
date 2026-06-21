# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest03638(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
