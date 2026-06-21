# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest10057(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
