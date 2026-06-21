# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest51650(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
