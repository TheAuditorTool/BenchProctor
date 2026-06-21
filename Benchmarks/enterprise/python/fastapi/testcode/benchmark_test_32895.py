# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest32895(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    os.remove(str(data))
    return {"updated": True}
