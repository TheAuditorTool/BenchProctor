# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest31940(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
