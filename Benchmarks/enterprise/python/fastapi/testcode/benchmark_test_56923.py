# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import time
from app_runtime import redis_client


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest56923(request: Request):
    redis_value = redis_client.get('user_data')
    data = handle(redis_value)
    if time.time() > 1000000000:
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
