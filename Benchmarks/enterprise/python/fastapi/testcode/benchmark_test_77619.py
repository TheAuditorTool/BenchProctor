# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest77619(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
