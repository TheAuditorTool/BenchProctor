# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest16316(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
