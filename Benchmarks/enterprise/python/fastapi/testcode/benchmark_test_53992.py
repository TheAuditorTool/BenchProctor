# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53992(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
