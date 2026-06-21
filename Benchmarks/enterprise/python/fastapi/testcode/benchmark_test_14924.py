# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest14924(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
