# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest70426(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
