# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest51391(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
