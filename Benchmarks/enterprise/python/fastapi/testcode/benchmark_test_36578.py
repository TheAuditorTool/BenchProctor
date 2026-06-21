# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36578(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
