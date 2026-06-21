# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest05098(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
