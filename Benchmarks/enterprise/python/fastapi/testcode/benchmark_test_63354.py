# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest63354(request: Request):
    host_value = request.headers.get('host', '')
    os.system('echo ' + str(host_value))
    return {"updated": True}
