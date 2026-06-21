# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest56118(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
