# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from types import SimpleNamespace


async def BenchmarkTest46922(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ns = SimpleNamespace(payload=yaml_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return {"updated": True}
