# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest59735(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
