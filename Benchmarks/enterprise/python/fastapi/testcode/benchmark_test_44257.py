# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest44257(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
