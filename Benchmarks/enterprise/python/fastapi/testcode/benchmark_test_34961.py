# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34961(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    eval(str(data))
    return {"updated": True}
