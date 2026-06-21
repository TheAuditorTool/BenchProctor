# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest32723(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return {"updated": True}
