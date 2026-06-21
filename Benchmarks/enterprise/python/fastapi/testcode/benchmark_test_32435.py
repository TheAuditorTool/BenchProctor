# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import db


async def BenchmarkTest32435(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
