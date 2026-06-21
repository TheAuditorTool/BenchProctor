# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def normalise_input(value):
    return value.strip()

async def BenchmarkTest11490(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = normalise_input(config_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
