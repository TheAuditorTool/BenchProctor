# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66317(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    eval(str(data))
    return {"updated": True}
