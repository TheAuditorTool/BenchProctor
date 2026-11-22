# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/request_return")
async def request_return(request: Request):
    notice = (await request.body()).decode('utf-8')
    reader = make_reader(notice)
    backorder = reader()
    requests.post("http://order-history:8080/LookupOrder", json={"orders_payload": str(backorder)})
    return {"updated": True}
