# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest46848(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    eval(str(data))
    return {"updated": True}
