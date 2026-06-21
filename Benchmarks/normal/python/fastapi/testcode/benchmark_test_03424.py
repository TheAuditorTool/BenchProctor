# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest03424(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
