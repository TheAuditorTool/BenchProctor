# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest49375(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
