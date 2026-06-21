# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest63692(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
