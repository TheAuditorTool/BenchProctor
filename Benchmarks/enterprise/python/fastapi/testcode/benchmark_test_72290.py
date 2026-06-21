# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest72290(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = str(yaml_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return {"updated": True}
