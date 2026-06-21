# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29779(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
