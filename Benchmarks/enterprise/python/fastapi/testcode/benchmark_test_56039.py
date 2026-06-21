# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest56039(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    os.system('echo ' + str(data))
    return {"updated": True}
