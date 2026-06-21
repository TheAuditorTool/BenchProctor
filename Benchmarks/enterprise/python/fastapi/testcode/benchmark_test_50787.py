# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50787(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
