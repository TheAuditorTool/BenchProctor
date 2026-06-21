# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest72926(request: Request):
    origin_value = request.headers.get('origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(origin_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = origin_value
    logging.info('User action: ' + str(processed))
    return {"updated": True}
