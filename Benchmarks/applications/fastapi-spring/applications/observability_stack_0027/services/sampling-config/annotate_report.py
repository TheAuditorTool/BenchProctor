# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
import json
from app_runtime import db


router = APIRouter()


@router.post("/annotate_report")
async def annotate_report(request: Request):
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        gauge = json.loads(remark).get('value', remark)
    except (json.JSONDecodeError, AttributeError):
        gauge = remark
    yaml.load(gauge, Loader=yaml.UnsafeLoader)
    return {"updated": True}
