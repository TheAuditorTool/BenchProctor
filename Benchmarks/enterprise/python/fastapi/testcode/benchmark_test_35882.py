# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest35882(request: Request):
    auth_header = request.headers.get('authorization', '')
    subprocess.run([str(auth_header), '--status'], shell=False)
    return {"updated": True}
