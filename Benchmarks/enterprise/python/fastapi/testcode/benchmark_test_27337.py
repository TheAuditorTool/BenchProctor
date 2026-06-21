# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27337(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
