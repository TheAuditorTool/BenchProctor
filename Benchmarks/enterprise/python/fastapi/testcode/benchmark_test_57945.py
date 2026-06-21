# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57945(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
