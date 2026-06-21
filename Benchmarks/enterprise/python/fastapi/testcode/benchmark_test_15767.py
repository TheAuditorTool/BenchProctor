# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15767(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
