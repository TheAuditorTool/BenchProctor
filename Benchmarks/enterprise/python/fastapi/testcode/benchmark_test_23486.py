# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23486(request: Request):
    user_id = request.query_params.get('id', '')
    if not str(user_id).isdigit():
        raise Exception('error: ' + str(user_id))
    return {"updated": True}
