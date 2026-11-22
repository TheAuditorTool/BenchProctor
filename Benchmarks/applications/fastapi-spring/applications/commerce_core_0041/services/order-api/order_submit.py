# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/place_order/{id}")
async def place_order(request: Request, id: str):
    headline = request.path_params.get('id', '')
    backorder = RequestPayload(headline).value
    requests.post("http://cart-service:8080/UpdateCart", json={"orders_payload": str(backorder)})
    return {"updated": True}
