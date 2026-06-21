# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest10931(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
