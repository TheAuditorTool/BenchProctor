# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os


async def BenchmarkTest34832(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '{}'.format(dotenv_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
