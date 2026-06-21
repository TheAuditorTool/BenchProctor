# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest46869(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
