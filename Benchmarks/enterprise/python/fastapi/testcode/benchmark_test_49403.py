# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49403(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    int(str(data))
    return {"updated": True}
