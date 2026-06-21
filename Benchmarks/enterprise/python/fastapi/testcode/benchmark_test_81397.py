# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, User


async def BenchmarkTest81397(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
