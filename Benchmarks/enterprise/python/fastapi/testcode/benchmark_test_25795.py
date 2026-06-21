# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25795(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
