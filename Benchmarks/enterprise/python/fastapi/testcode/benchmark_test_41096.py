# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest41096(request: Request):
    query_array = request.query_params.get('items', '')
    data, _sep, _rest = str(query_array).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
