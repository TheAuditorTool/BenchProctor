# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69685(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    request.session['data'] = str(data)
    return {"updated": True}
