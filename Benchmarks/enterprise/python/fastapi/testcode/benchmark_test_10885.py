# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest10885(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    os.system('echo ' + str(forwarded_ip))
    return {"updated": True}
