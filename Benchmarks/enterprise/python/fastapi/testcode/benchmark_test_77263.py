# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77263(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    eval(str(data))
    return {"updated": True}
