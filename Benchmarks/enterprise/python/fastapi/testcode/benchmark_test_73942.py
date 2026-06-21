# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


async def BenchmarkTest73942(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
