# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest07704(request: Request):
    referer_value = request.headers.get('referer', '')
    defusedxml.ElementTree.fromstring(str(referer_value))
    return {"updated": True}
