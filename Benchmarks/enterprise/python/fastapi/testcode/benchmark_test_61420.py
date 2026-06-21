# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest61420(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = FormData(payload=yaml_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
