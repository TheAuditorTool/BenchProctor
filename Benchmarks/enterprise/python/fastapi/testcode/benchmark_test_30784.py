# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest30784(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
