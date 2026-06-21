# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest13493(request: Request):
    user_id = request.query_params.get('id', '')
    defusedxml.ElementTree.fromstring(str(user_id))
    return {"updated": True}
