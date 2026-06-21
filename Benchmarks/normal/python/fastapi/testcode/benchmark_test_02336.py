# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02336(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
