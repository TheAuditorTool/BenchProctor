# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07199(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
