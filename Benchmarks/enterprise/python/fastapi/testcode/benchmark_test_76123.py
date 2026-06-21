# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
from types import SimpleNamespace


async def BenchmarkTest76123(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return {"updated": True}
