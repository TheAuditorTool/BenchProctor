# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from app_runtime import redis_client


async def BenchmarkTest39916(request: Request):
    redis_value = redis_client.get('user_data')
    data = '%s' % (redis_value,)
    yaml.safe_load(data)
    return {"updated": True}
