# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest19672(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
