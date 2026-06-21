# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, User


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest49002(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
