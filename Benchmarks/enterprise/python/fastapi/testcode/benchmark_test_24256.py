# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest24256(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
