# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest58590(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    subprocess.run('echo ' + str(raw_body), shell=True)
    return {"updated": True}
