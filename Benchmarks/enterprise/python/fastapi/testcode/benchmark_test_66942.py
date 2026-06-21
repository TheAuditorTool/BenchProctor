# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest66942(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
