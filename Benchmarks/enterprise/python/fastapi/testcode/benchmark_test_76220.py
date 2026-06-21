# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


async def BenchmarkTest76220(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    prefix = ''
    data = prefix + str(dotenv_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
