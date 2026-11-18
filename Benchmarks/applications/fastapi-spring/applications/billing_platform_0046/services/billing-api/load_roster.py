# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import socket


router = APIRouter()


@router.post("/load_roster")
async def load_roster(request: Request):
    remark = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    s = socket.create_connection((str(remittance), 80))
    s.close()
    return {"updated": True}
