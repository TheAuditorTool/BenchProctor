# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest78961(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    int(str(data))
    return {"updated": True}
