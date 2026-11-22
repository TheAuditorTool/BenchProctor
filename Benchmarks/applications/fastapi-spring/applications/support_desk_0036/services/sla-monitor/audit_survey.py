# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/audit_survey")
async def audit_survey(request: Request):
    preface = request.headers.get('user-agent', '')
    requests.get(str(preface))
    return {"updated": True}
