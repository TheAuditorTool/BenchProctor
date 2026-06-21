# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest66992(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
