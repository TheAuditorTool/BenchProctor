# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest64375(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
