# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest04162(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
