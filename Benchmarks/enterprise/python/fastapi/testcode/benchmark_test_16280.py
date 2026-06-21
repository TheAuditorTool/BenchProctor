# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest16280(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
