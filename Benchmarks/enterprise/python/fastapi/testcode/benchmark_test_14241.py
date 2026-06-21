# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest14241(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
