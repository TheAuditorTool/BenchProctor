# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest68606(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    if len(str(data)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
