# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest68345(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
