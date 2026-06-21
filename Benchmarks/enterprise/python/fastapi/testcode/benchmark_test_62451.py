# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62451(request: Request):
    user_id = request.query_params.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    int(str(data))
    return {"updated": True}
