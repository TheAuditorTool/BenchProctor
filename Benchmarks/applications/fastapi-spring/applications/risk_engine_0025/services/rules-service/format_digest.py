# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
import json
from app_runtime import db


router = APIRouter()


@router.post("/format_digest")
async def format_digest(request: Request):
    excerpt = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        verdict = json.loads(excerpt).get('value', excerpt)
    except (json.JSONDecodeError, AttributeError):
        verdict = excerpt
    yaml.load(verdict, Loader=yaml.UnsafeLoader)
    return {"updated": True}
