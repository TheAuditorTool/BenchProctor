# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest37511(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = default_blank(auth_header)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
