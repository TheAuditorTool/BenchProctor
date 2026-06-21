# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import redis_client


async def BenchmarkTest73774(request: Request):
    redis_value = redis_client.get('user_data')
    data, _sep, _rest = str(redis_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
