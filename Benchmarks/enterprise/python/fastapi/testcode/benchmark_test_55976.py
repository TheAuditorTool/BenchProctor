# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55976(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
