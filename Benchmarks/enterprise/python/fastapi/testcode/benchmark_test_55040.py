# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, User


async def BenchmarkTest55040(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
