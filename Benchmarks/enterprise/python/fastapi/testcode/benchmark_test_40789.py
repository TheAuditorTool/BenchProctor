# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40789(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
