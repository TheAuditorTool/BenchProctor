# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest06169(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    os.remove(str(data))
    return {"updated": True}
