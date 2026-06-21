# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest02133(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
