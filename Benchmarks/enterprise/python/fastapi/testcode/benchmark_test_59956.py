# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def relay_value(value):
    return value

async def BenchmarkTest59956(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
