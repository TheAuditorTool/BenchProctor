# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest30237(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
