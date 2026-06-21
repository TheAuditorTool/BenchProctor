# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest81219(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
