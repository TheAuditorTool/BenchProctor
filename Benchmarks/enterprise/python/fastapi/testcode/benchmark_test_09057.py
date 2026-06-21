# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest09057(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
