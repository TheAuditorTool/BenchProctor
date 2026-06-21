# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest10324(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
