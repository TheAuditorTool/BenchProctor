# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


async def BenchmarkTest67302(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    logging.info('User action: ' + str(dotenv_value))
    return {"updated": True}
