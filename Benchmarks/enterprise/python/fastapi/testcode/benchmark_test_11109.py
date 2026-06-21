# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import pickle
from app_runtime import redis_client


async def BenchmarkTest11109(request: Request):
    redis_value = redis_client.get('user_data')
    data = json.loads(redis_value).get('value', '')
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
