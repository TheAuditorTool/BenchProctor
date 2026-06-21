# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest63561(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
