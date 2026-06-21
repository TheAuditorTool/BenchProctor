# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


async def BenchmarkTest74864(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
