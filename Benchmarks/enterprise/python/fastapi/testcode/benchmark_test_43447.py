# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest43447(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
