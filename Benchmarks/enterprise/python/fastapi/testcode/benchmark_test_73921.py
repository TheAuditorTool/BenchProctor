# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest73921(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
