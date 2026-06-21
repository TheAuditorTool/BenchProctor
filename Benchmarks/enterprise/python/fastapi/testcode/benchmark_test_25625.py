# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest25625(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
