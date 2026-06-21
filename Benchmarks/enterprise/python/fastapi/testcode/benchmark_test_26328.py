# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26328(request: Request):
    user_id = request.query_params.get('id', '')
    exec(str(user_id))
    return {"updated": True}
