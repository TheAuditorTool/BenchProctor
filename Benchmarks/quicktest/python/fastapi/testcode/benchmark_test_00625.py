# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest00625(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = coalesce_blank(ua_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
