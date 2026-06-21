# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest36407(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
