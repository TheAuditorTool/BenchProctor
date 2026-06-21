# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01064(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    os.seteuid(65534)
    return {"updated": True}
