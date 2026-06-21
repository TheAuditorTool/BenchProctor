# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest49591(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return {"updated": True}
