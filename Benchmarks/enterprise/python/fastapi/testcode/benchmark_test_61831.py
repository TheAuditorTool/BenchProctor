# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61831(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
