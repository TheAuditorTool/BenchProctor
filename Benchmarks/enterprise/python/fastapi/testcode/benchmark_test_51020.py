# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest51020(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
