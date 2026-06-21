# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29107(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    result = 100 / int(str(data))
    return {"updated": True}
