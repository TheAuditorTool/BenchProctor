# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json


async def BenchmarkTest01055(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
