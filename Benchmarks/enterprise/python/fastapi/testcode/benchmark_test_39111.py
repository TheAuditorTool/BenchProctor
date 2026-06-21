# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


async def BenchmarkTest39111(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    logging.info('User action: ' + str(env_value))
    return {"updated": True}
