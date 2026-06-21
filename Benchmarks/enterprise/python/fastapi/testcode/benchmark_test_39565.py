# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39565(request: Request):
    user_id = request.query_params.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    exec(str(data))
    return {"updated": True}
