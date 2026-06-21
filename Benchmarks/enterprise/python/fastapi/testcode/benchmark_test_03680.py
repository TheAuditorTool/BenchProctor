# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03680(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
