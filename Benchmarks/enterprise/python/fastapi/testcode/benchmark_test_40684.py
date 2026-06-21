# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest40684(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
