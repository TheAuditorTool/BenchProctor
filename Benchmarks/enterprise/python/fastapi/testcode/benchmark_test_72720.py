# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest72720(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
