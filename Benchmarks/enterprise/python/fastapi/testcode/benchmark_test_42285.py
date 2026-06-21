# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest42285(request: Request):
    upload_name = (await request.form()).get('upload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
