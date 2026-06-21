# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest10652(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
