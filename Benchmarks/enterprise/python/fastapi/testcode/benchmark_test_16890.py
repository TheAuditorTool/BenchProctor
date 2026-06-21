# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest16890(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    os.system('echo ' + str(raw_body))
    return {"updated": True}
