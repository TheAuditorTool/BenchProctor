# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest78873(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
