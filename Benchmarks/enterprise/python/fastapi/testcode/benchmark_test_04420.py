# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time
from app_runtime import db


async def BenchmarkTest04420(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
