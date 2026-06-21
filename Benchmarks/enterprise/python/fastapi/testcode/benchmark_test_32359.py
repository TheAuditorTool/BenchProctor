# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import sys
from starlette.responses import JSONResponse
import json


async def BenchmarkTest32359(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    try:
        data = json.loads(argv_value).get('value', argv_value)
    except (json.JSONDecodeError, AttributeError):
        data = argv_value
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content
