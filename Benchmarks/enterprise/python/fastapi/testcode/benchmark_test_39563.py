# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest39563(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
