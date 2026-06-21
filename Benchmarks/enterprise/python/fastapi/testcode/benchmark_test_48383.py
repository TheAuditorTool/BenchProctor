# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48383(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    eval(str(data))
    return {"updated": True}
