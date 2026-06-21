# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import redis_client


async def BenchmarkTest47226(request: Request):
    redis_value = redis_client.get('user_data')
    kind = 'json' if str(redis_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = redis_value
            data = parsed
        case _:
            data = redis_value
    json.loads(data)
    return {"updated": True}
