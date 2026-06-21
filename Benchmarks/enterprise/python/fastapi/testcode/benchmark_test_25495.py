# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


request_state: dict[str, str] = {}

async def BenchmarkTest25495(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return {"updated": True}
