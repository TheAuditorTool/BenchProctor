# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest09488(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    yaml.safe_load(data)
    return {"updated": True}
