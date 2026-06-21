# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from app_runtime import auth_check


async def BenchmarkTest39238(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
