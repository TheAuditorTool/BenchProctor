# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import redis_client


async def BenchmarkTest05518(request: Request):
    redis_value = redis_client.get('user_data')
    data = f'{redis_value:.200s}'
    json.loads(data)
    return {"updated": True}
