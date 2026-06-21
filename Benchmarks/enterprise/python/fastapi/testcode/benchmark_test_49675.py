# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest49675(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = coalesce_blank(yaml_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
