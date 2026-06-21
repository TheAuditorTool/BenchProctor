# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23165(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
