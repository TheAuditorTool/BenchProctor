# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest16623(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    os.system('echo ' + str(data))
    return {"updated": True}
