# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest07592(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ' '.join(str(auth_header).split())
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
