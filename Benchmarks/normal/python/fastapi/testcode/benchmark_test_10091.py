# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import db, User


async def BenchmarkTest10091(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
