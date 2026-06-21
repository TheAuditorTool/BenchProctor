# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest68050(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
