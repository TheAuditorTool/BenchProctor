# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest57970(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
