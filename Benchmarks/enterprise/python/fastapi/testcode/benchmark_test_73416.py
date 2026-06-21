# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest73416(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
