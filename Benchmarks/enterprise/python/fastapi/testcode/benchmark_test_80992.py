# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


request_state: dict[str, str] = {}

async def BenchmarkTest80992(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return {"updated": True}
