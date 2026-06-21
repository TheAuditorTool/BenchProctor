# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest16754(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = FormData(payload=config_value).payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
