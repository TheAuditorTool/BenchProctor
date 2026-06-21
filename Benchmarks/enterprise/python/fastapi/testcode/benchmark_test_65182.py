# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest65182(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
