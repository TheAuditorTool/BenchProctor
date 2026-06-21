# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest34067(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
