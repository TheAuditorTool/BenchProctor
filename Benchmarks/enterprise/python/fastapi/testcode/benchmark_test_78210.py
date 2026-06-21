# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest78210(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    subprocess.Popen('echo ' + str(raw_body), shell=True).wait()
    return {"updated": True}
