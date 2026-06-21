# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import base64


async def BenchmarkTest58016(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
