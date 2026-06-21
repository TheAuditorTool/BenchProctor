# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest56355(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
