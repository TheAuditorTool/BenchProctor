# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import redis_client


async def BenchmarkTest62550(request: Request):
    redis_value = redis_client.get('user_data')
    data = '%s' % (redis_value,)
    json.loads(data)
    return {"updated": True}
