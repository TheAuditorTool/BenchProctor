# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05971(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '{}'.format(header_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
