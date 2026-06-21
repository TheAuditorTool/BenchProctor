# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02012(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
