# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest31090(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
