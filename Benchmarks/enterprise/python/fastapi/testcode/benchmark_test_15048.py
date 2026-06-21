# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import defusedxml.ElementTree


async def BenchmarkTest15048(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
