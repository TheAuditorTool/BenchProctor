# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest48505(request: Request):
    host_value = request.headers.get('host', '')
    data = coalesce_blank(host_value)
    os.remove(str(data))
    return {"updated": True}
