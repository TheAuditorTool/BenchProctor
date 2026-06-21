# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


async def BenchmarkTest06773(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
