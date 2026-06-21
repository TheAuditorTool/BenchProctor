# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05492(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
