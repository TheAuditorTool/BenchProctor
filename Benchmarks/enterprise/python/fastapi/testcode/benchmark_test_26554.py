# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest26554(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    os.remove(str(data))
    return {"updated": True}
