# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00367(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    eval(str(data))
    return {"updated": True}
