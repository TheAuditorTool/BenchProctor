# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest18025(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
