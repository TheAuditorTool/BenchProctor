# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest23226(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
