# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest08473(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
