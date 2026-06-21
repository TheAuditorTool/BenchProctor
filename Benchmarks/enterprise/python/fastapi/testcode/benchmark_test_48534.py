# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48534(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
