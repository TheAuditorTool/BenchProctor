# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51832(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    result = 100 / int(str(data))
    return {"updated": True}
