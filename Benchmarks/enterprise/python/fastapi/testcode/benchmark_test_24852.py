# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db, User


async def BenchmarkTest24852(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
