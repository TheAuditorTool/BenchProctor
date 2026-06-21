# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest60263(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    logging.info('User action: ' + str(data))
    return {"updated": True}
