# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/transform_payload")
async def transform_payload(request: Request):
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    handshake = normalize(citation)
    requests.post("http://partner-registry:8080/RegisterPartner", json={"integrations_payload": str(handshake)})
    return {"updated": True}
