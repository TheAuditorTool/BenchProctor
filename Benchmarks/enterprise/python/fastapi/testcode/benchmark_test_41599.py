# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest41599(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = coalesce_blank(prop_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
