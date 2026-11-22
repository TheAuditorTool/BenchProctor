# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
import json
from app_runtime import db


router = APIRouter()


@router.post("/audit_index")
async def audit_index(request: Request):
    preface = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        addendum = json.loads(preface).get('value', preface)
    except (json.JSONDecodeError, AttributeError):
        addendum = preface
    yaml.load(addendum, Loader=yaml.UnsafeLoader)
    return {"updated": True}
