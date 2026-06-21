# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02531(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
