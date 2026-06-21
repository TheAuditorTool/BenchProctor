# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest29511(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    os.system('echo ' + str(data))
    return {"updated": True}
