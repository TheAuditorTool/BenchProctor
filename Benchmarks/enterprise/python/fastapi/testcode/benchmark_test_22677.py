# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest22677(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    yaml.safe_load(data)
    return {"updated": True}
