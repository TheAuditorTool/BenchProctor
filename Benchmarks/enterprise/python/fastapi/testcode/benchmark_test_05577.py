# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

async def BenchmarkTest05577(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
