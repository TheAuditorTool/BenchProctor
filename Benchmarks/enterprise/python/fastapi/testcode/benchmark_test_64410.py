# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64410(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
