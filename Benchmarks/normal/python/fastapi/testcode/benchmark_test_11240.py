# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


async def BenchmarkTest11240(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
