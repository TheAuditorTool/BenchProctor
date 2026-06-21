# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, User


async def BenchmarkTest25903(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    db.session.query(User).filter(User.id == header_value).all()
    return {"updated": True}
