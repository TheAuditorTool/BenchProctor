# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import redis_client


async def BenchmarkTest03299(request: Request):
    redis_value = redis_client.get('user_data')
    try:
        data = json.loads(redis_value).get('value', redis_value)
    except (json.JSONDecodeError, AttributeError):
        data = redis_value
    json.loads(data)
    return {"updated": True}
