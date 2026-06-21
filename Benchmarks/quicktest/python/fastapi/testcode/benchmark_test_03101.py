# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03101(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
