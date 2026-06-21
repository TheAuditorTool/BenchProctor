# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09720(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    auth_check('user', data)
    return {"updated": True}
