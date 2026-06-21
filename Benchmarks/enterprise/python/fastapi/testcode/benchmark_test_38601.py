# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest38601(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    exec(str(data))
    return {"updated": True}
