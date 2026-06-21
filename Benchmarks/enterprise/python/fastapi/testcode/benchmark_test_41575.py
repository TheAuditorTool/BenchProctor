# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest41575(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
