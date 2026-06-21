# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01982(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
