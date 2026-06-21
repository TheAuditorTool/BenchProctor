# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36294(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    result = 100 / int(str(data))
    return {"updated": True}
