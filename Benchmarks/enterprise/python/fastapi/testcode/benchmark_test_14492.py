# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest14492(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    os.system('echo ' + str(data))
    return {"updated": True}
