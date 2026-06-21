# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest57921(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    os.system('echo ' + str(data))
    return {"updated": True}
