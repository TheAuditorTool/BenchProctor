# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest23301(request: Request):
    ua_value = request.headers.get('user-agent', '')
    defusedxml.ElementTree.fromstring(str(ua_value))
    return {"updated": True}
