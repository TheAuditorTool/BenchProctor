# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest25364(request: Request):
    stdin_value = input('input: ')
    if stdin_value:
        data = stdin_value
    else:
        data = ''
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
