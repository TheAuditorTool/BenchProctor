# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest56137(request: Request):
    stdin_value = input('input: ')
    data, _sep, _rest = str(stdin_value).partition('\x00')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
