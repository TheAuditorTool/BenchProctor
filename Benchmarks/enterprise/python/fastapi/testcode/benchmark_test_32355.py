# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest32355(request: Request):
    stdin_value = input('input: ')
    ctx = RequestContext(stdin_value)
    data = ctx.payload
    eval(compile("subprocess.Popen('echo ' + str(data), shell=True).wait()", '<sink>', 'exec'))
    return {"updated": True}
