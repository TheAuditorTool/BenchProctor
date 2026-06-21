# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest63652(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
