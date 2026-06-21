# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest53013(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
