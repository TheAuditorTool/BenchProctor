# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

async def BenchmarkTest59246(request: Request):
    host_value = request.headers.get('host', '')
    data = to_text(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
