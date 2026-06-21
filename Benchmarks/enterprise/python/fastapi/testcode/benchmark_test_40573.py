# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest40573(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
