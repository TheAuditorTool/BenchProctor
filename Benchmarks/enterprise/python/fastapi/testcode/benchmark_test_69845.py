# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest69845(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
