# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel
import json


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest13486(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
