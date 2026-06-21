# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest65977(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
