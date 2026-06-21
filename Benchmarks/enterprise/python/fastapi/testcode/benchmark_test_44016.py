# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest44016(request: Request):
    query_array = request.query_params.get('items', '')
    data = FormData(payload=query_array).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
