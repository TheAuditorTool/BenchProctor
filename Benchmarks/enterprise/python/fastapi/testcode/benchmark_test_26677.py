# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest26677(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = coalesce_blank(dotenv_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
