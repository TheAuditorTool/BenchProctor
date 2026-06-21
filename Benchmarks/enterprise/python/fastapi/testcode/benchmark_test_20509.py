# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, User


async def BenchmarkTest20509(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
