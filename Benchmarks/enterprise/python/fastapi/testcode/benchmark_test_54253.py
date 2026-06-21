# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest54253(request: Request, field: str = Form('')):
    field_value = field
    db.execute('SELECT * FROM users WHERE id = ' + str(field_value))
    return {"updated": True}
