# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest40620(request: Request):
    stdin_value = input('input: ')
    ctx = RequestContext(stdin_value)
    data = ctx.payload
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
