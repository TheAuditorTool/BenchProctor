# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80889(request: Request):
    user_id = request.query_params.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
