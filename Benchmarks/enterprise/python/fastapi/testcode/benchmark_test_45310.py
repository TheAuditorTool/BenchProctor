# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45310(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
