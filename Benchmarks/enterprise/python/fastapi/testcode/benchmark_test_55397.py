# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest55397(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
