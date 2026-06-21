# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78781(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
