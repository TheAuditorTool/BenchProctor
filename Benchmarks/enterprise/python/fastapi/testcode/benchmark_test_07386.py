# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


async def BenchmarkTest07386(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value:.200s}'
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
