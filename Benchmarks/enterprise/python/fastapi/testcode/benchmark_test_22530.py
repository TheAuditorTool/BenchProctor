# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22530(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
