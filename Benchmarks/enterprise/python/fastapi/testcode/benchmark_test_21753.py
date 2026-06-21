# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest21753(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
