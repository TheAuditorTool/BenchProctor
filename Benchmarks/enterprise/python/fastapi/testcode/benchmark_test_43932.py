# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest43932(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    subprocess.run([str(header_value), '--status'], shell=False)
    return {"updated": True}
