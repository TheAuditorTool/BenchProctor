# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07838(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
