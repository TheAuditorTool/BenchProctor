# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import base64
import pickle


router = APIRouter()


@router.post("/collect_header")
async def collect_header(request: Request):
    summary = (await request.json()).get('payload', '')
    try:
        grievance = json.loads(summary).get('value', summary)
    except (json.JSONDecodeError, AttributeError):
        grievance = summary
    pickle.loads(base64.b64decode(grievance))
    return {"updated": True}
