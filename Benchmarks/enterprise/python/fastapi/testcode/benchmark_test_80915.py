# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest80915(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
