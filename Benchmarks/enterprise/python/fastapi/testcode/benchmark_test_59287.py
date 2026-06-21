# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import redis_client


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest59287(request: Request):
    redis_value = redis_client.get('user_data')
    data = coalesce_blank(redis_value)
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return {"updated": True}
