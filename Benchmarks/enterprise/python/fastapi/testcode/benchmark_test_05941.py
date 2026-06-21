# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest05941(request: Request):
    stdin_value = input('input: ')
    data, _sep, _rest = str(stdin_value).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
