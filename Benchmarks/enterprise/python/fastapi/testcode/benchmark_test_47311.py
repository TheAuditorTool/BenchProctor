# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


async def BenchmarkTest47311(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(config_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
