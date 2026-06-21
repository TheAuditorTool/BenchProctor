# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest17267(request: Request):
    host_value = request.headers.get('host', '')
    os.remove(str(host_value))
    return {"updated": True}
