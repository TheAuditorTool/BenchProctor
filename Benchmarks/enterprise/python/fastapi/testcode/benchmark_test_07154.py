# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from app_runtime import redis_client


async def BenchmarkTest07154(request: Request):
    redis_value = redis_client.get('user_data')
    data = json.loads(redis_value).get('value', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
