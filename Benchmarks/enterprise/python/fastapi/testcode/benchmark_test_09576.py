# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, User


async def BenchmarkTest09576(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
