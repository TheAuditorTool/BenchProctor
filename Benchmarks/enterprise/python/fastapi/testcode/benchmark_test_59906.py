# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest59906(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
