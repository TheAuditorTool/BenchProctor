# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest37668(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    logging.info('User action: ' + str(data))
    return {"updated": True}
