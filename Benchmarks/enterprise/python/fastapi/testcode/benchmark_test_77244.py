# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest77244(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ' '.join(str(raw_body).split())
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
