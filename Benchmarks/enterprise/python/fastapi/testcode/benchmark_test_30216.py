# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30216(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
