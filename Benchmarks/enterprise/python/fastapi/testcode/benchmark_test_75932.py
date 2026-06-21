# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest75932(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
