# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import redis_client


async def BenchmarkTest55073(request: Request):
    redis_value = redis_client.get('user_data')
    data = (lambda v: v.strip())(redis_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
