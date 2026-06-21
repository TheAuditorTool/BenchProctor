# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import time


request_state: dict[str, str] = {}

async def BenchmarkTest48643(request: Request):
    stdin_value = input('input: ')
    request_state['last_input'] = stdin_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
