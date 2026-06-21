# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06825(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
