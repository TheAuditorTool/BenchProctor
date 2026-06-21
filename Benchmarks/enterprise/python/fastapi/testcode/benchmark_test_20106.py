# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest20106(request: Request):
    origin_value = request.headers.get('origin', '')
    defusedxml.ElementTree.fromstring(str(origin_value))
    return {"updated": True}
