# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest00302(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
