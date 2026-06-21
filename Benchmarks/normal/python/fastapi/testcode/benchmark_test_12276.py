# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import defusedxml.ElementTree
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest12276(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
