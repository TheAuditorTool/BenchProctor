# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest44348(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
