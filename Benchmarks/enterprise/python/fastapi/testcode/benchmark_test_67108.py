# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest67108(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
