# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest14749(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    os.remove(str(data))
    return {"updated": True}
