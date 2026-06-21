# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

async def BenchmarkTest60212(request: Request):
    path_value = request.path_params.get('id', '')
    data = to_text(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
