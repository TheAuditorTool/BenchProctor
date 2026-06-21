# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest73144(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
