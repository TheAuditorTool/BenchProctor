# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
import json
from app_runtime import db


router = APIRouter()


@router.post("/rotate_threshold")
async def rotate_threshold(request: Request):
    memo = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        ledger = json.loads(memo).get('value', memo)
    except (json.JSONDecodeError, AttributeError):
        ledger = memo
    yaml.load(ledger, Loader=yaml.UnsafeLoader)
    return {"updated": True}
