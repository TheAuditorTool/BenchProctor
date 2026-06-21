# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os


async def BenchmarkTest57501(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
