# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest02869(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
