# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
import json
from app_runtime import db


router = APIRouter()


@router.post("/annotate_snapshot")
async def annotate_snapshot(request: Request):
    footnote = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        remittance = json.loads(footnote).get('value', footnote)
    except (json.JSONDecodeError, AttributeError):
        remittance = footnote
    yaml.load(remittance, Loader=yaml.UnsafeLoader)
    return {"updated": True}
