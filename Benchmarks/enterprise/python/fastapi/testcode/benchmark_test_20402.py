# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import base64


async def BenchmarkTest20402(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
