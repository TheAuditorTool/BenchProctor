# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest04863(request: Request):
    referer_value = request.headers.get('referer', '')
    reader = make_reader(referer_value)
    data = reader()
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
