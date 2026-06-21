# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import redis_client


async def BenchmarkTest32727(request: Request):
    redis_value = redis_client.get('user_data')
    data = ' '.join(str(redis_value).split())
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
