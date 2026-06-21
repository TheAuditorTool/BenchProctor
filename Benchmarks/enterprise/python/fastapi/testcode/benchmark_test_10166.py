# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest10166(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
