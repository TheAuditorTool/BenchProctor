# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest45499(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
