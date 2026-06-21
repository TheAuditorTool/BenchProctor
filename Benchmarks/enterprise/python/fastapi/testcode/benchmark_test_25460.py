# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest25460(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
