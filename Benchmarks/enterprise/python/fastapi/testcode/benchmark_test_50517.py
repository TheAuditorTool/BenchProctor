# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest50517(request: Request):
    referer_value = request.headers.get('referer', '')
    data = FormData(payload=referer_value).payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
