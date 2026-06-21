# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


async def BenchmarkTest59043(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
