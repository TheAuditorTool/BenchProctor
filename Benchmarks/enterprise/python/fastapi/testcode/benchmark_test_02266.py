# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest02266(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
