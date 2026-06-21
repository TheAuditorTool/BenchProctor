# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest76552(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = header_value
    logging.info('User action: ' + str(processed))
    return {"updated": True}
