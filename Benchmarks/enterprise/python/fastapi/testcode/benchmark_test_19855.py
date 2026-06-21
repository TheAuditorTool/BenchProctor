# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19855(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
