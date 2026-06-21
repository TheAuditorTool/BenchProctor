# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78170(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
