# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import redis_client


async def BenchmarkTest34749(request: Request):
    redis_value = redis_client.get('user_data')
    def normalize(value):
        return value.strip()
    data = normalize(redis_value)
    requests.get(str(data))
    return {"updated": True}
