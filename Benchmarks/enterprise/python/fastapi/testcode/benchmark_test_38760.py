# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse
import json


async def BenchmarkTest38760(request: Request):
    query_array = request.query_params.get('items', '')
    try:
        data = json.loads(query_array).get('value', query_array)
    except (json.JSONDecodeError, AttributeError):
        data = query_array
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
