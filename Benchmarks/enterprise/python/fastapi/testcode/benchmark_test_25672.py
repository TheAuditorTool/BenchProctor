# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25672(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    result = 100 / int(str(data))
    return {"updated": True}
