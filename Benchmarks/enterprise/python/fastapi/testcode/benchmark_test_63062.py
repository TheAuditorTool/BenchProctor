# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest63062(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    logging.info('User action: ' + str(config_value))
    return {"updated": True}
