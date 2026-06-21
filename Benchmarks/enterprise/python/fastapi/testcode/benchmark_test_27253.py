# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27253(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    eval(str(data))
    return {"updated": True}
