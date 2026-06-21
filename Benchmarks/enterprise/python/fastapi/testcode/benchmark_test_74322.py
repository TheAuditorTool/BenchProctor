# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74322(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    int(str(data))
    return {"updated": True}
