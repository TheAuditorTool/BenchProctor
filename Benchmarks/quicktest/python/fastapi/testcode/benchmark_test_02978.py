# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02978(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
