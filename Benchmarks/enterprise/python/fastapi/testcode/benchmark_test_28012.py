# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest28012(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    os.system('echo ' + str(data))
    return {"updated": True}
