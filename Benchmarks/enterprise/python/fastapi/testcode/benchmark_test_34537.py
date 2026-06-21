# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest34537(request: Request):
    host_value = request.headers.get('host', '')
    defusedxml.ElementTree.fromstring(str(host_value))
    return {"updated": True}
