# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33194(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    int(str(data))
    return {"updated": True}
