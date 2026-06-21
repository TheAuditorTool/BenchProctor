# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from app_runtime import db


async def BenchmarkTest63417(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return {"updated": True}
