# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest64874(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
