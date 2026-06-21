# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest10243(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
