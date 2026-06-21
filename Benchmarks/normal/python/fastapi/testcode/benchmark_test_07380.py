# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest07380(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    importlib.import_module(str(data))
    return {"updated": True}
