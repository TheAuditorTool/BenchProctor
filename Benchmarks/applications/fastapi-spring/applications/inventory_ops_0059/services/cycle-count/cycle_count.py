# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json
from app_runtime import db


router = APIRouter()


@router.post("/run_cycle_count")
async def run_cycle_count(request: Request):
    memo = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        backorder = json.loads(memo).get('value', memo)
    except (json.JSONDecodeError, AttributeError):
        backorder = memo
    requests.post("http://supplier-feed:8080/PullSupplierFeed", json={"inventory_payload": str(backorder)})
    return {"updated": True}
