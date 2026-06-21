# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest41846(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
