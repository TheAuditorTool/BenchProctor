# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13427(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
