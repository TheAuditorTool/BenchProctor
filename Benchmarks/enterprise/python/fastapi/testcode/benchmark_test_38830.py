# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


async def BenchmarkTest38830(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    if dotenv_value:
        data = dotenv_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return {"updated": True}
