# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import redis_client


async def BenchmarkTest01274(request: Request):
    redis_value = redis_client.get('user_data')
    data = redis_value.decode('utf-8', 'ignore') if isinstance(redis_value, bytes) else redis_value
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
