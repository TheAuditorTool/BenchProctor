# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest48086(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    eval(str(data))
    return {"updated": True}
