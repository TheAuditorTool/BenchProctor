# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest53717(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
