# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08062(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
