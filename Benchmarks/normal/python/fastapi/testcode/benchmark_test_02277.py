# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import redis_client


async def BenchmarkTest02277(request: Request):
    redis_value = redis_client.get('user_data')
    data = redis_value if redis_value else 'default'
    yaml.safe_load(data)
    return {"updated": True}
