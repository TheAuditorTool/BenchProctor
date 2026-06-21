# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest48215(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
