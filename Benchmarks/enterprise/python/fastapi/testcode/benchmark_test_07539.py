# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import redis_client


async def BenchmarkTest07539(request: Request):
    redis_value = redis_client.get('user_data')
    parts = str(redis_value).split(',')
    data = ','.join(parts)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
