# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51944(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    exec(str(data))
    return {"updated": True}
