# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest71285(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
