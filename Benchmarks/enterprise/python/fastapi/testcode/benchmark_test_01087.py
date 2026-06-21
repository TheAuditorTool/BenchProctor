# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01087(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
