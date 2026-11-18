# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json


router = APIRouter()


@router.post("/build_manifest")
async def build_manifest(request: Request):
    footnote = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        consignment = json.loads(footnote).get('value', footnote)
    except (json.JSONDecodeError, AttributeError):
        consignment = footnote
    requests.post("http://label-service:8080/CreateLabel", json={"shipping_payload": str(consignment)})
    return {"updated": True}
