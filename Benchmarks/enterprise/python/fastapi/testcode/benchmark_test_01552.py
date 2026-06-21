# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db, User


async def BenchmarkTest01552(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
