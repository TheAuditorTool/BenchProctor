# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


async def BenchmarkTest49666(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(prop_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
