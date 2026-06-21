# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest00607(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(yaml_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
