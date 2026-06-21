# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18319(request: Request):
    user_id = request.query_params.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
