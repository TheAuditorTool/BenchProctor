# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest43227(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    async def _evasion_task():
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    await _evasion_task()
    return {"updated": True}
