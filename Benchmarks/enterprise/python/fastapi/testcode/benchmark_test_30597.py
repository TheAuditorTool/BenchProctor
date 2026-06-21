# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30597(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
