# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest45444(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
