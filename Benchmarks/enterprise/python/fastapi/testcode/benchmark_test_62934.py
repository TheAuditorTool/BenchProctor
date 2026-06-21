# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62934(request: Request):
    host_value = request.headers.get('host', '')
    int(str(host_value))
    return {"updated": True}
