# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest07652(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
