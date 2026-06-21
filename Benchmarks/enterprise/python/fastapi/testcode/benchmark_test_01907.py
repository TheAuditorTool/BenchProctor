# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest01907(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data, _sep, _rest = str(config_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return {"updated": True}
