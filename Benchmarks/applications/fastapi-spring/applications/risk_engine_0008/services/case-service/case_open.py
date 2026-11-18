# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/open_case")
async def open_case(request: Request):
    synopsis = db.fetch_one('SELECT text FROM comments LIMIT 1')
    verdict = f'{synopsis!s}'
    requests.post("http://decision-log:8080/RecordDecision", json={"risk_payload": str(verdict)})
    return {"updated": True}
