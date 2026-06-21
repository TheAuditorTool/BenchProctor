# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest52412(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
