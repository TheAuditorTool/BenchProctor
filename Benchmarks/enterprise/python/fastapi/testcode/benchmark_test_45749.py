# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45749(request: Request):
    origin_value = request.headers.get('origin', '')
    data = bytearray(int(origin_value) if str(origin_value).isdigit() else 0)
    return {"updated": True}
