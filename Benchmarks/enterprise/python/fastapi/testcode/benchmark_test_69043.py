# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest69043(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    os.system('echo ' + str(data))
    return {"updated": True}
