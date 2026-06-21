# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest40334(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
