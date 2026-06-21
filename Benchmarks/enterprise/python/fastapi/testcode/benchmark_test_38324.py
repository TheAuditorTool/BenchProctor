# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38324(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
