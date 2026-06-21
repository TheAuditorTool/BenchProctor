# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39523(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
