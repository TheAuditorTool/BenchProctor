# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest62135(request: Request):
    auth_header = request.headers.get('authorization', '')
    defusedxml.ElementTree.fromstring(str(auth_header))
    return {"updated": True}
