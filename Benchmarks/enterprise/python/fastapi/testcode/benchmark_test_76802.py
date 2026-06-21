# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import defusedxml.ElementTree


async def BenchmarkTest76802(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
