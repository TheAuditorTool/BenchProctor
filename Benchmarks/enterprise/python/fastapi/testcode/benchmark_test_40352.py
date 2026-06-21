# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest40352(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
