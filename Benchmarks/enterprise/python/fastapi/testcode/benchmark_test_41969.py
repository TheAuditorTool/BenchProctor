# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest41969(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
