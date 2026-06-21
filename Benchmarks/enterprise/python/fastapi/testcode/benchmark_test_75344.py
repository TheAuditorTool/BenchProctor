# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
import json


async def BenchmarkTest75344(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
