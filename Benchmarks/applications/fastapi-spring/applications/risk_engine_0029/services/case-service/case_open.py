# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from starlette.responses import JSONResponse
from app_runtime import db


router = APIRouter()


@router.post("/open_case")
async def open_case(request: Request):
    subject = db.fetch_one('SELECT text FROM comments LIMIT 1')
    grievance = str(subject).replace('\x00', '')
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    requests.post("http://screening-service:8080/RunScreening", json={"risk_payload": str(grievance)})
    return {"updated": True}
