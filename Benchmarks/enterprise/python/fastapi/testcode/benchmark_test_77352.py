# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77352(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    result = 100 / int(str(data))
    return {"updated": True}
