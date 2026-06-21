# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest57448(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
