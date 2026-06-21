# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, User


async def BenchmarkTest32447(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
