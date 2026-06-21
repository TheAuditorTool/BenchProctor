# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest34746(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = '{}'.format(yaml_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
