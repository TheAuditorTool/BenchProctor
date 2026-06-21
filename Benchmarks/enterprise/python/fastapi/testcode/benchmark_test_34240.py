# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import json


async def BenchmarkTest34240(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
