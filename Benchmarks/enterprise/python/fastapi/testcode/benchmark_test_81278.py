# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest81278(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
