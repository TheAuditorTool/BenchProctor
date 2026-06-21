# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest00821(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
