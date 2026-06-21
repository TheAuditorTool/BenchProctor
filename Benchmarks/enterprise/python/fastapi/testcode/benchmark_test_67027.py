# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest67027(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
