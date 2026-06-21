# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest61150(request: Request):
    referer_value = request.headers.get('referer', '')
    subprocess.run('echo ' + str(referer_value), shell=True)
    return {"updated": True}
