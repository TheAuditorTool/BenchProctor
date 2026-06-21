# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest49567(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    globals()['counter'] = int(data)
    return {"updated": True}
