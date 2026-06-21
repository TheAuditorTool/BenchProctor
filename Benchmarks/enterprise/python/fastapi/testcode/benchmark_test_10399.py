# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest10399(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
