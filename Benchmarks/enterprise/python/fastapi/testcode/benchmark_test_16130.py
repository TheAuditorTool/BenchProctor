# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest16130(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    auth_check('user', data)
    return {"updated": True}
