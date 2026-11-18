# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/audit_report")
async def audit_report(request: Request):
    heading = (await request.body()).decode('utf-8')
    consignment = '{}'.format(heading)
    requests.get(str(consignment))
    return {"updated": True}
