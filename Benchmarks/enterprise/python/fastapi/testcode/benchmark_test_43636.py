# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


async def BenchmarkTest43636(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % (forwarded_ip,)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
