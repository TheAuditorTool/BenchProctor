# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73481(request: Request):
    user_id = request.query_params.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
