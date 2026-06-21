# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06338(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = FormData(payload=config_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
