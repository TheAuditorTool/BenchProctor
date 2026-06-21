# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest75320(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = RequestPayload(comment_value).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
