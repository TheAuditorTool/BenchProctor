# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77266(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    eval(str(data))
    return {"updated": True}
