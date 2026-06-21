# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, User


async def BenchmarkTest52027(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
