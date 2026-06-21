# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import redis_client


async def BenchmarkTest10153(request: Request):
    redis_value = redis_client.get('user_data')
    if redis_value:
        data = redis_value
    else:
        data = ''
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
