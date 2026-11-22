# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
import json
from app_runtime import db


router = APIRouter()


@router.post("/publish_checkpoint")
async def publish_checkpoint(request: Request):
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        persona = json.loads(remark).get('value', remark)
    except (json.JSONDecodeError, AttributeError):
        persona = remark
    yaml.load(persona, Loader=yaml.UnsafeLoader)
    return {"updated": True}
