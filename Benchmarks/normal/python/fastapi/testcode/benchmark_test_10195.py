# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest10195(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
