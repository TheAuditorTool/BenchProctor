# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30188(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    int(str(data))
    return {"updated": True}
