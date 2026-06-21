# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest13919(request: Request):
    stdin_value = input('input: ')
    data = ' '.join(str(stdin_value).split())
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
