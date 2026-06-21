# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest26610(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
