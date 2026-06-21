# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel
from types import SimpleNamespace


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04668(request: Request, req: UserInput):
    json_value = req.payload
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return {"updated": True}
