# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55008(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
