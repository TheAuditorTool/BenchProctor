# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json
from app_runtime import db


router = APIRouter()


@router.post("/store_archive")
async def store_archive(request: Request):
    wording = db.fetch_one('SELECT name FROM users LIMIT 1')
    addendum = json.loads(wording).get('value', '')
    requests.post("http://document-api:8080/UploadDocument", json={"documents_payload": str(addendum)})
    return {"updated": True}
