# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest23169(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
