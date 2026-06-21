# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest33342(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = FormData(payload=upload_name).payload
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
