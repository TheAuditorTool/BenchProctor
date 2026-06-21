# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19193(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    exec(str(data))
    return {"updated": True}
