# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20132(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    int(str(data))
    return {"updated": True}
