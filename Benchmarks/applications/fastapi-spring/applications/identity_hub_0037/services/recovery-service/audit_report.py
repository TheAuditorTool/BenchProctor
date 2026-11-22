# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/audit_report")
async def audit_report(request: Request):
    remark = request.headers.get('user-agent', '')
    requests.get(str(remark))
    return {"updated": True}
