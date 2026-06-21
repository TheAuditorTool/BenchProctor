# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest80945(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
