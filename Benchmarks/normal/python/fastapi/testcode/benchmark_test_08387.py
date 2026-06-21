# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest08387(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = default_blank(forwarded_ip)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
