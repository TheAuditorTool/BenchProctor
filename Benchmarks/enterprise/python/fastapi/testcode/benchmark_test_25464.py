# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest25464(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
