# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import redis_client


async def BenchmarkTest75903(request: Request):
    redis_value = redis_client.get('user_data')
    data = redis_value.decode('utf-8', 'ignore') if isinstance(redis_value, bytes) else redis_value
    json.loads(data)
    return {"updated": True}
