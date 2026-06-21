# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest76378(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = ' '.join(str(config_value).split())
    logging.info('User action: ' + str(data))
    return {"updated": True}
