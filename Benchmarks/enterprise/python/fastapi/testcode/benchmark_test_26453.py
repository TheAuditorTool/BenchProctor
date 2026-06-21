# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest26453(request: Request):
    path_value = request.path_params.get('id', '')
    defusedxml.ElementTree.fromstring(str(path_value))
    return {"updated": True}
