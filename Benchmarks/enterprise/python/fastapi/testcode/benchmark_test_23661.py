# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest23661(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
