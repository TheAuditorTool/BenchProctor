# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest33435(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
