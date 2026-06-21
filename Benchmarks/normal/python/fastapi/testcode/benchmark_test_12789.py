# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest12789(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
