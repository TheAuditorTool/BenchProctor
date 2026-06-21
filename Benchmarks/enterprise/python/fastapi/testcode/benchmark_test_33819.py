# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest33819(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
