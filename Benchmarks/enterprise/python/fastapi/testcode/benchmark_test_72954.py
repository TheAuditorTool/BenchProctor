# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest72954(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
