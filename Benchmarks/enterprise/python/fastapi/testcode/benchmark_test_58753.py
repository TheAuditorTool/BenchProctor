# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58753(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    int(str(data))
    return {"updated": True}
