# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest37032(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
