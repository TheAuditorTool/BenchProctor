# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest18284(request: Request):
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
