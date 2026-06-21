# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest05494(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    os.system('echo ' + str(data))
    return {"updated": True}
