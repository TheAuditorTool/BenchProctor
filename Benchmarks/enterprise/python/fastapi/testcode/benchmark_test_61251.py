# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest61251(request: Request):
    query_array = request.query_params.get('items', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(query_array)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = query_array
    logging.info('User action: ' + str(processed))
    return {"updated": True}
