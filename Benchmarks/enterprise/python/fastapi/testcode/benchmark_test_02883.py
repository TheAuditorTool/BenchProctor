# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest02883(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    logging.info('User action: ' + str(prop_value))
    return {"updated": True}
