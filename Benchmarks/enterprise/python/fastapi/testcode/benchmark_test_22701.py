# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import json
from app_runtime import redis_client


async def BenchmarkTest22701(request: Request):
    redis_value = redis_client.get('user_data')
    data = base64.b64decode(redis_value).decode('utf-8', 'ignore')
    json.loads(data)
    return {"updated": True}
