# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest54433(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
