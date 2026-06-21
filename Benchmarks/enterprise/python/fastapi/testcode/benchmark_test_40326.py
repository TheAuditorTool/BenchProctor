# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest40326(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
