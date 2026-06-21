# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import auth_check


async def BenchmarkTest69019(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    auth_check('user', data)
    return {"updated": True}
