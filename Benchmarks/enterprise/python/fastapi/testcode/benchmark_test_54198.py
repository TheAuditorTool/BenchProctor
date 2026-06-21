# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54198(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
