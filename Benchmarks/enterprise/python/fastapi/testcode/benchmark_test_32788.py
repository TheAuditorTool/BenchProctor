# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest32788(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    globals()['counter'] = int(data)
    return {"updated": True}
