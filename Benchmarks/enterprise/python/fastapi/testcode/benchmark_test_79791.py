# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79791(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % (raw_body,)
    eval(str(data))
    return {"updated": True}
