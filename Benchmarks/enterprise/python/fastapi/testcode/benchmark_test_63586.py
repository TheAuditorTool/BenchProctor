# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63586(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    int(str(data))
    return {"updated": True}
