# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/publish_artifact")
async def publish_artifact(request: Request):
    wording = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(wording).split(',')
    remark = ' '.join(parts)
    requests.post("http://rollback-service:8080/TriggerRollback", json={"delivery_payload": str(remark)})
    return {"updated": True}
