# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27014(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
