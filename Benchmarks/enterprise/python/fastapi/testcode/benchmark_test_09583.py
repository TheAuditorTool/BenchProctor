# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest09583(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
