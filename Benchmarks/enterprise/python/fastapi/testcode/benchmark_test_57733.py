# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest57733(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    os.system('echo ' + str(data))
    return {"updated": True}
