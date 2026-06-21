# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03264(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
