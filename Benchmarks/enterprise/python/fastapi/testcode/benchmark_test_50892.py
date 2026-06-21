# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest50892(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    logging.info('User action: ' + str(db_value))
    return {"updated": True}
