# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66528(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    result = 100 / int(str(data))
    return {"updated": True}
