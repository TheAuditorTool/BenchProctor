# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
from types import SimpleNamespace


async def BenchmarkTest71414(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return {"updated": True}
