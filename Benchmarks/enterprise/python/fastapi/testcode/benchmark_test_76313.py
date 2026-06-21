# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76313(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
