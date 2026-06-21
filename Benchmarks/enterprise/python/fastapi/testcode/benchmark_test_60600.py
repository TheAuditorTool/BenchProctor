# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

async def BenchmarkTest60600(request: Request):
    path_value = request.path_params.get('id', '')
    data = normalise_input(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
