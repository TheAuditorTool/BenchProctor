# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest47861(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
