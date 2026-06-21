# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

async def BenchmarkTest09266(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
