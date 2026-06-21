# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import redis_client


async def BenchmarkTest59719(request: Request):
    redis_value = redis_client.get('user_data')
    pickle.loads(redis_value.encode('latin-1'))
    return {"updated": True}
