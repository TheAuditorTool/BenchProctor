# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest56677(request: Request):
    stdin_value = input('input: ')
    data = stdin_value if stdin_value else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
