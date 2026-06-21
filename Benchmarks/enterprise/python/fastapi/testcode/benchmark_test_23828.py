# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest23828(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
