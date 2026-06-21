# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest36544(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return {"updated": True}
