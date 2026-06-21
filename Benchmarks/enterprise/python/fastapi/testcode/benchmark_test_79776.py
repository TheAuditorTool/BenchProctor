# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, User


async def BenchmarkTest79776(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
