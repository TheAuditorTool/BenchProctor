# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db, User


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest47321(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
