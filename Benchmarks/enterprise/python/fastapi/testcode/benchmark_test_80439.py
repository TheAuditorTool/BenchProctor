# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


request_state: dict[str, str] = {}

async def BenchmarkTest80439(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
