# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest01771(request: Request):
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
