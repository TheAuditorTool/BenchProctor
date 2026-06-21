# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest64932(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
