# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


def ensure_str(value):
    return str(value)

async def BenchmarkTest40221(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = ensure_str(yaml_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
