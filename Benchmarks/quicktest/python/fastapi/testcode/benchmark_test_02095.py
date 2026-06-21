# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, User


async def BenchmarkTest02095(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
