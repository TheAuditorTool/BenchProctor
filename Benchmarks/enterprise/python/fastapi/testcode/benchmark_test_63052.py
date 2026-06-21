# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import base64


async def BenchmarkTest63052(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
