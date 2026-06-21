# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import base64


async def BenchmarkTest23928(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
