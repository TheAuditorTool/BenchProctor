# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66025(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
