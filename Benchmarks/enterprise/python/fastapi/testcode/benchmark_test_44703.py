# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest44703(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
