# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest05846(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
