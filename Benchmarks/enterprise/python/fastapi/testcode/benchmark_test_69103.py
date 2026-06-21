# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69103(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
