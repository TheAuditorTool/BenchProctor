# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest40312(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
