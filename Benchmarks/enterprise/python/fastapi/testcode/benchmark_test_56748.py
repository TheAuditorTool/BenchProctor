# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest56748(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    result = 100 / int(str(data))
    return {"updated": True}
