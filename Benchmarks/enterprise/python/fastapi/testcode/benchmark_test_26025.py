# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest26025(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
