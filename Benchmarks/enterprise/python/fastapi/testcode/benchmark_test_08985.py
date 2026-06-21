# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest08985(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
