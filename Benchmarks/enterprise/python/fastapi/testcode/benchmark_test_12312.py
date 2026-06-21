# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import tempfile
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest12312(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
