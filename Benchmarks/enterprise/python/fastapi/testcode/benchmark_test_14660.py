# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, User


async def BenchmarkTest14660(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
