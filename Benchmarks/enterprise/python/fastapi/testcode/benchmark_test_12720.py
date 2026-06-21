# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest12720(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return {"updated": True}
