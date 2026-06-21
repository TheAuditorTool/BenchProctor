# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


async def BenchmarkTest06691(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
