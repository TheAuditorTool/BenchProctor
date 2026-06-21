# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


async def BenchmarkTest20980(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = (lambda v: v.strip())(yaml_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
