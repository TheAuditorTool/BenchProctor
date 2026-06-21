# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09030(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
