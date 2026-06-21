# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from app_runtime import db


async def BenchmarkTest02808(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    yaml.safe_load(comment_value)
    return {"updated": True}
