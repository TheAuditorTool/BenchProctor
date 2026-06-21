# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51492(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    result = 100 / int(str(data))
    return {"updated": True}
