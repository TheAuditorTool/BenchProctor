# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest14599(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
