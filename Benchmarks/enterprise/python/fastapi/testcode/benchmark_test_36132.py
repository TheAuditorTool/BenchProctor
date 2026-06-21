# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest36132(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
