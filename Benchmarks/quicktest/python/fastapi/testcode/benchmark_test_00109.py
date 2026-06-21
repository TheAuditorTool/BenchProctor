# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest00109(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
