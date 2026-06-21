# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest45335(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
