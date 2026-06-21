# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70736(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
