# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest08232(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    logging.info('User action: ' + str(data))
    return {"updated": True}
